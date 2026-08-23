from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]
EXPORT_MANIFEST = ROOT / ".github" / "public-release.json"
EXPECTED_CONTENT_FILES = 389
EXPECTED_OPERATIONAL_FILES = 6
EXPECTED_PAPER_PAGES = 176
EXPECTED_PAPER_IMAGES = 172
EXPECTED_PROJECTS = 194
EXPECTED_TRACK_COUNTS = {
    "### 1. 动作数据与重定向": (14, 13),
    "### 2. Locomotion与运动先验": (38, 30),
    "### 3. 动作跟踪与全身控制": (37, 27),
    "### 4. LocoManip与物理交互": (30, 23),
    "### 5. 世界模型、VLA与Agent": (40, 21),
    "### 6. 工程与实机部署": (17, 80),
}
PAGES_WITHOUT_EMBEDDED_FIGURES = {
    "P016.md",
    "P135.md",
    "P144.md",
    "P152.md",
    "P164.md",
    "P165.md",
    "P166.md",
    "P167.md",
    "P168.md",
    "P169.md",
    "P170.md",
    "P171.md",
    "P172.md",
}
RUNTIME_IGNORED_DIRS = {".git", "__pycache__"}
RUNTIME_IGNORED_SUFFIXES = {".pyc"}
ALLOWED_TOP_LEVEL = {
    ".gitattributes",
    ".github",
    ".gitignore",
    "AGENTS.md",
    "README.md",
    "LICENSE.md",
    "公司与产业",
    "技术路线",
    "求职与岗位",
    "论文与项目",
}
ALLOWED_GITHUB_FILES = {
    Path(".github/public-release.json"),
    Path(".github/scripts/validate_public_tree.py"),
    Path(".github/workflows/public-release-check.yml"),
    Path(".github/ISSUE_TEMPLATE/论文或技术报告候选.yml"),
    Path(".github/ISSUE_TEMPLATE/开源项目候选或复现结果.yml"),
    Path(".github/ISSUE_TEMPLATE/事实分类与技术解释纠错.yml"),
    Path(".github/ISSUE_TEMPLATE/链接失效或招聘状态变化.yml"),
}
FORBIDDEN_PARTS = {
    "99_维护与协作",
    "__MACOSX",
    "backups",
    "output",
    "tmp",
}
FORBIDDEN_SUFFIXES = {
    ".7z",
    ".bak",
    ".csv",
    ".dmg",
    ".gz",
    ".ppt",
    ".pptx",
    ".rar",
    ".tar",
    ".tgz",
    ".tmp",
    ".tsv",
    ".xls",
    ".xlsx",
    ".zip",
}
LINK_RE = re.compile(r"(!?\[[^\]]*\]\()([^)]+)(\))")
SKIP_LINK_PREFIXES = ("http://", "https://", "mailto:", "#", "data:")
IMAGE_SUFFIXES = {".gif", ".jpeg", ".jpg", ".png", ".webp"}
READER_INTERNAL_RE = re.compile(
    r"私有源库|白名单导出|维护者|用户提供|内部备注|交叉核验|"
    r"维护数据|维护层|编辑备注|本轮覆盖快照|更新节奏|\.csv` 生成"
)
PUBLIC_MAINTENANCE_FIELD_RE = re.compile(
    r"^last_verified:\s*|最后更新时间|最后更新：|最近核验：|核验日期|"
    r"时间为(?:最后|最近一次)核验日期",
    flags=re.MULTILINE,
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def collect_files(errors: list[str]) -> list[Path]:
    files: list[Path] = []
    for current, directories, names in os.walk(ROOT, followlinks=False):
        current_path = Path(current)
        for name in list(directories):
            candidate = current_path / name
            relative = candidate.relative_to(ROOT)
            if name in RUNTIME_IGNORED_DIRS:
                directories.remove(name)
            elif candidate.is_symlink():
                errors.append(f"公开仓库禁止符号链接目录：{relative}")
                directories.remove(name)
        for name in names:
            candidate = current_path / name
            relative = candidate.relative_to(ROOT)
            if candidate.suffix.lower() in RUNTIME_IGNORED_SUFFIXES:
                continue
            if candidate.is_symlink():
                errors.append(f"公开仓库禁止符号链接文件：{relative}")
                continue
            files.append(candidate)
    return sorted(files)


def clean_target(raw: str) -> str:
    value = raw.strip()
    if value.startswith("<") and ">" in value:
        value = value[1:value.index(">")]
    elif " " in value:
        value = value.split(" ", 1)[0]
    return unquote(value.split("#", 1)[0])


def check_paths(files: list[Path], errors: list[str]) -> None:
    top_level = {
        child.name for child in ROOT.iterdir()
        if child.name not in RUNTIME_IGNORED_DIRS
    }
    if top_level != ALLOWED_TOP_LEVEL:
        errors.append(
            "公开顶层白名单不一致；"
            f"缺少={sorted(ALLOWED_TOP_LEVEL - top_level)}；"
            f"多余={sorted(top_level - ALLOWED_TOP_LEVEL)}"
        )
    github_files = {
        path.relative_to(ROOT) for path in files
        if path.relative_to(ROOT).parts[0] == ".github"
    }
    if github_files != ALLOWED_GITHUB_FILES:
        errors.append(
            "GitHub运行文件白名单不一致；"
            f"缺少={sorted(ALLOWED_GITHUB_FILES - github_files)}；"
            f"多余={sorted(github_files - ALLOWED_GITHUB_FILES)}"
        )
    for path in files:
        relative = path.relative_to(ROOT)
        if any(part in FORBIDDEN_PARTS or part.startswith("._") for part in relative.parts):
            errors.append(f"公开仓库含维护层或系统路径：{relative}")
        if path.name in {".DS_Store", "Thumbs.db"}:
            errors.append(f"公开仓库含系统文件：{relative}")
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"公开仓库含源文档、数据表或压缩包：{relative}")


def check_export_manifest(files: list[Path], errors: list[str]) -> None:
    if not EXPORT_MANIFEST.is_file():
        errors.append("缺少.github/public-release.json")
        return
    try:
        payload = json.loads(EXPORT_MANIFEST.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f".github/public-release.json无法读取：{exc}")
        return
    if payload.get("schema_version") != 1:
        errors.append(".github/public-release.json schema_version必须为1")
    records = payload.get("files")
    if not isinstance(records, list):
        errors.append(".github/public-release.json files必须为列表")
        return
    by_path: dict[Path, dict[str, object]] = {}
    for record in records:
        if not isinstance(record, dict) or not isinstance(record.get("path"), str):
            errors.append(".github/public-release.json含非法记录")
            continue
        relative = Path(record["path"])
        if relative.is_absolute() or ".." in relative.parts:
            errors.append(f".github/public-release.json含非法路径：{relative}")
            continue
        if relative in by_path:
            errors.append(f".github/public-release.json含重复路径：{relative}")
        by_path[relative] = record

    actual = {
        path.relative_to(ROOT) for path in files
        if path != EXPORT_MANIFEST
    }
    if set(by_path) != actual:
        errors.append(
            "公开仓库与导出清单不一致；"
            f"未登记={sorted(actual - set(by_path))}；"
            f"缺失={sorted(set(by_path) - actual)}"
        )
    for relative, record in by_path.items():
        path = ROOT / relative
        if not path.is_file():
            continue
        if record.get("size") != path.stat().st_size:
            errors.append(f"文件大小偏离导出结果：{relative}")
        if record.get("sha256") != sha256(path):
            errors.append(f"文件内容偏离导出结果：{relative}")

    content_count = sum(path.parts[0] != ".github" for path in actual)
    operational_count = len(actual) - content_count
    if content_count != EXPECTED_CONTENT_FILES:
        errors.append(
            f"公开读者内容应为{EXPECTED_CONTENT_FILES}个文件，实际为{content_count}"
        )
    if operational_count != EXPECTED_OPERATIONAL_FILES:
        errors.append(
            f"公开运行文件应为{EXPECTED_OPERATIONAL_FILES}个，实际为{operational_count}"
        )
    if payload.get("content_file_count") != content_count:
        errors.append("导出清单content_file_count与实际不一致")
    if payload.get("operational_file_count") != operational_count:
        errors.append("导出清单operational_file_count与实际不一致")


def check_markdown(files: list[Path], errors: list[str]) -> None:
    root_resolved = ROOT.resolve()
    referenced_images: set[Path] = set()
    markdown_files = [path for path in files if path.suffix.lower() == ".md"]
    for page in markdown_files:
        text = page.read_text(encoding="utf-8")
        for match in PUBLIC_MAINTENANCE_FIELD_RE.finditer(text):
            line_no = text.count("\n", 0, match.start()) + 1
            errors.append(
                f"{page.relative_to(ROOT)}:{line_no} 含公开层维护时间字段：{match.group(0)}"
            )
        for match in READER_INTERNAL_RE.finditer(text):
            line_no = text.count("\n", 0, match.start()) + 1
            errors.append(
                f"{page.relative_to(ROOT)}:{line_no} 含内部维护口吻：{match.group(0)}"
            )
        for line_no, line in enumerate(text.splitlines(), 1):
            for match in LINK_RE.finditer(line):
                raw = match.group(2)
                if raw.startswith(SKIP_LINK_PREFIXES):
                    continue
                target = clean_target(raw)
                if not target:
                    continue
                resolved = (page.parent / target).resolve()
                try:
                    relative = resolved.relative_to(root_resolved)
                except ValueError:
                    errors.append(
                        f"{page.relative_to(ROOT)}:{line_no} 链接越出公开仓库：{raw}"
                    )
                    continue
                if not resolved.exists():
                    errors.append(
                        f"{page.relative_to(ROOT)}:{line_no} 链接不存在：{raw}"
                    )
                elif "![" in match.group(1) and resolved.is_file():
                    referenced_images.add(relative)

    paper_dir = ROOT / "论文与项目" / "论文逐篇解读"
    paper_pages = sorted(paper_dir.glob("P[0-9][0-9][0-9].md"))
    expected_names = {f"P{number:03d}.md" for number in range(1, EXPECTED_PAPER_PAGES + 1)}
    actual_names = {path.name for path in paper_pages}
    if actual_names != expected_names:
        errors.append(
            "论文页面集合不完整；"
            f"缺少={sorted(expected_names - actual_names)}；"
            f"多余={sorted(actual_names - expected_names)}"
        )
    for page in paper_pages:
        text = page.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append(f"论文页面缺少front matter：{page.relative_to(ROOT)}")
        for field in ("title", "track"):
            if not re.search(rf"^{field}:\s*\S", text, flags=re.MULTILINE):
                errors.append(f"论文页面缺少{field}：{page.relative_to(ROOT)}")
        if page.name not in PAGES_WITHOUT_EMBEDDED_FIGURES and "![" not in text:
            errors.append(f"论文页面缺少论文图片：{page.relative_to(ROOT)}")

    paper_images = {
        path.relative_to(ROOT) for path in files
        if path.suffix.lower() in IMAGE_SUFFIXES
        and (ROOT / "论文与项目" / "论文逐篇解读" / "论文原图") in path.parents
    }
    if len(paper_images) != EXPECTED_PAPER_IMAGES:
        errors.append(
            f"论文图片应为{EXPECTED_PAPER_IMAGES}张，实际为{len(paper_images)}张"
        )
    orphaned = sorted(paper_images - referenced_images)
    if orphaned:
        errors.append(f"存在未被论文页面引用的图片：{orphaned}")


def check_readme_counts(errors: list[str]) -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    headings = list(EXPECTED_TRACK_COUNTS)
    for index, heading in enumerate(headings):
        start = readme.find(heading)
        end = (
            readme.find(headings[index + 1], start)
            if index + 1 < len(headings)
            else readme.find("## 新手学习顺序", start)
        )
        papers, projects = EXPECTED_TRACK_COUNTS[heading]
        expected = f"完整页面收录**{papers}篇论文/技术报告和{projects}个项目**"
        if start == -1 or end == -1 or expected not in readme[start:end]:
            errors.append(f"README路线数量与公开数据不一致：{heading}；expected={expected}")
    for expected in (
        f"{EXPECTED_PAPER_PAGES}篇论文与技术报告按最终系统作用分类",
        f"{EXPECTED_PROJECTS}个项目的研发位置、关键实现、开源边界与开发价值",
    ):
        if expected not in readme:
            errors.append(f"README总数与公开数据不一致：expected={expected}")


def main() -> None:
    errors: list[str] = []
    files = collect_files(errors)
    check_paths(files, errors)
    check_export_manifest(files, errors)
    check_markdown(files, errors)
    check_readme_counts(errors)
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        raise SystemExit(1)
    print(
        "Public repository validation passed: "
        f"content={EXPECTED_CONTENT_FILES}, operational={EXPECTED_OPERATIONAL_FILES}, "
        f"papers={EXPECTED_PAPER_PAGES}, paper_images={EXPECTED_PAPER_IMAGES}, "
        "hash manifest and internal links verified."
    )


if __name__ == "__main__":
    main()
