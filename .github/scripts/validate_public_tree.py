from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit


ROOT = Path(__file__).resolve().parents[2]
EXPORT_MANIFEST = ROOT / ".github" / "public-release.json"
EXPECTED_CONTENT_FILES = 710
EXPECTED_OPERATIONAL_FILES = 6
EXPECTED_PAPER_PAGES = 467
EXPECTED_PAPER_IMAGES = 201
EXPECTED_PAPER_IDS = set('P001 P002 P003 P004 P005 P006 P007 P008 P009 P010 P011 P012 P013 P014 P015 P016 P017 P018 P019 P020 P021 P022 P023 P024 P025 P026 P027 P028 P029 P030 P031 P032 P033 P034 P035 P036 P037 P038 P039 P040 P041 P042 P043 P044 P045 P046 P047 P048 P049 P050 P051 P052 P053 P054 P055 P056 P057 P058 P059 P060 P061 P062 P063 P064 P065 P066 P067 P068 P069 P070 P071 P072 P073 P074 P075 P076 P077 P078 P079 P080 P081 P082 P083 P084 P085 P086 P087 P088 P089 P090 P091 P092 P093 P094 P095 P096 P097 P098 P099 P100 P101 P102 P103 P104 P105 P106 P107 P108 P109 P110 P111 P112 P113 P114 P115 P116 P117 P118 P119 P120 P121 P122 P123 P124 P125 P126 P127 P128 P129 P130 P131 P132 P133 P134 P135 P136 P137 P138 P139 P140 P141 P142 P143 P144 P145 P146 P147 P148 P149 P150 P151 P152 P153 P154 P155 P156 P157 P158 P159 P160 P161 P162 P163 P164 P165 P166 P167 P168 P169 P170 P171 P172 P173 P174 P175 P176 P177 P178 P179 P180 P181 P182 P183 P184 P185 P186 P187 P188 P189 P190 P191 P192 P193 P194 P195 P196 P197 P198 P199 P200 P201 P202 P203 P204 P205 P206 P207 P208 P209 P210 P211 P212 P213 P214 P215 P216 P217 P218 P219 P220 P221 P222 P223 P224 P225 P226 P227 P228 P229 P230 P231 P232 P233 P234 P236 P237 P238 P239 P240 P241 P242 P243 P244 P245 P246 P247 P248 P249 P250 P251 P252 P253 P254 P255 P256 P257 P258 P259 P260 P261 P262 P263 P264 P265 P266 P267 P273 P274 P275 P276 P277 P278 P279 P285 P286 P287 P288 P289 P290 P291 P292 P293 P294 P295 P304 P305 P306 P307 P308 P309 P310 P280 P268 P269 P270 P271 P272 P281 P282 P283 P284 P296 P297 P298 P299 P311 P312 P313 P300 P301 P302 P303 P314 P315 P316 P317 P318 P319 P320 P321 P322 P323 P324 P325 P326 P327 P328 P329 P330 P331 P332 P333 P335 P336 P337 P338 P339 P340 P341 P342 P343 P344 P345 P346 P347 P348 P349 P350 P351 P352 P353 P354 P355 P356 P357 P358 P359 P360 P361 P362 P363 P364 P365 P366 P367 P368 P369 P370 P371 P372 P373 P374 P375 P376 P377 P378 P379 P380 P381 P382 P383 P384 P385 P386 P387 P388 P389 P390 P391 P392 P393 P394 P395 P396 P397 P398 P399 P400 P401 P402 P403 P404 P405 P406 P407 P408 P409 P410 P411 P412 P413 P414 P415 P416 P417 P418 P419 P420 P427 P428 P429 P430 P431 P432 P433 P434 P435 P437 P439 P421 P422 P424 P425 P426 P438 P465 P466 P467 P468 P469 P470 P440 P441 P442 P443 P444 P445 P446 P447 P448 P449 P450 P451 P452 P453 P454 P455 P456 P457 P458 P459 P460 P461 P462 P463 P464 P471'.split())
EXPECTED_PROJECTS = 767
EXPECTED_DATASETS = 51
EXPECTED_TRACK_COUNTS = {
    "动作数据与重定向": (36, 67),
    "Locomotion与运动先验": (62, 79),
    "动作跟踪与全身控制": (48, 55),
    "LocoManip": (53, 52),
    "世界模型、VLA与Agent": (229, 196),
    "工程与实机部署": (39, 318),
}
PAGES_WITHOUT_EMBEDDED_FIGURES = set('P016.md P135.md P144.md P152.md P164.md P165.md P166.md P167.md P168.md P169.md P170.md P171.md P172.md P179.md P184.md P185.md P188.md P210.md P211.md P212.md P213.md P214.md P215.md P216.md P217.md P218.md P219.md P220.md P221.md P222.md P223.md P224.md P225.md P226.md P227.md P228.md P229.md P230.md P231.md P232.md P233.md P234.md P236.md P237.md P238.md P239.md P240.md P241.md P242.md P243.md P244.md P245.md P246.md P247.md P248.md P249.md P250.md P251.md P252.md P253.md P254.md P255.md P256.md P257.md P258.md P259.md P260.md P261.md P262.md P263.md P264.md P265.md P266.md P267.md P268.md P269.md P270.md P271.md P272.md P273.md P274.md P275.md P276.md P277.md P278.md P279.md P280.md P281.md P282.md P283.md P284.md P285.md P286.md P287.md P288.md P289.md P290.md P291.md P292.md P293.md P294.md P295.md P296.md P297.md P298.md P299.md P300.md P301.md P302.md P303.md P304.md P305.md P306.md P307.md P308.md P309.md P310.md P311.md P312.md P313.md P314.md P315.md P316.md P317.md P318.md P319.md P320.md P321.md P322.md P323.md P324.md P325.md P326.md P327.md P328.md P329.md P330.md P331.md P332.md P333.md P335.md P336.md P337.md P338.md P339.md P340.md P341.md P342.md P343.md P344.md P345.md P346.md P347.md P348.md P349.md P350.md P351.md P352.md P353.md P354.md P355.md P356.md P357.md P358.md P359.md P360.md P361.md P362.md P363.md P364.md P365.md P366.md P367.md P368.md P369.md P370.md P371.md P372.md P373.md P374.md P375.md P376.md P377.md P378.md P379.md P380.md P381.md P382.md P383.md P384.md P385.md P386.md P387.md P388.md P389.md P390.md P391.md P392.md P393.md P394.md P395.md P396.md P397.md P398.md P399.md P400.md P401.md P402.md P403.md P404.md P405.md P406.md P407.md P408.md P409.md P410.md P411.md P412.md P413.md P414.md P415.md P416.md P417.md P418.md P419.md P420.md P421.md P422.md P424.md P425.md P426.md P427.md P428.md P429.md P430.md P431.md P432.md P433.md P434.md P435.md P437.md P438.md P439.md P440.md P441.md P442.md P443.md P444.md P445.md P446.md P447.md P448.md P449.md P450.md P451.md P452.md P453.md P454.md P455.md P456.md P457.md P458.md P459.md P460.md P461.md P462.md P463.md P464.md P465.md P466.md P467.md P468.md P469.md P470.md P471.md'.split())
RUNTIME_IGNORED_DIRS = {".git", "__pycache__"}
RUNTIME_IGNORED_SUFFIXES = {".pyc"}
ALLOWED_TOP_LEVEL = {
    ".gitattributes",
    ".github",
    ".gitignore",
    "AGENTS.md",
    "README.md",
    "LICENSE.md",
    "具身智能公司的开源项目.md",
    "强化学习开发者必备开源资料",
    "公司与产品主表.md",
    "数据集",
    "技术与研究",
    "求职与岗位",
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
PROJECT_STATUS_FIELD_RE = re.compile(
    r"^#{1,6}[^\n]*(?:当前开放边界|开源状态|开放情况|开放范围|发布状态)|"
    r"\|\s*(?:开源|开放状态|代码状态|权重状态|许可记录|核验)\s*\||"
    r"\*\*(?:已公开内容|开放情况|关键限制|许可记录)\*\*|"
    r"(?:代码|权重)(?:仍|尚)?(?:未|待)(?:发布|开放|开源)|"
    r"(?:代码|权重)(?:已发布|已开放)",
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
        relative = page.relative_to(ROOT)
        if relative.parts[0] in {"技术与研究", "技术与研究", "数据集", "强化学习开发者必备开源资料", "具身智能公司的开源项目.md", "公司与产品主表.md"} and "许可" not in relative.parts:
            for match in PROJECT_STATUS_FIELD_RE.finditer(text):
                line_no = text.count("\n", 0, match.start()) + 1
                errors.append(f"{relative}:{line_no} 项目页面应展示用途与链接，不展示开放状态字段：{match.group(0)}")
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

    paper_dir = ROOT / "技术与研究" / "论文逐篇解读"
    paper_pages = sorted(paper_dir.glob("P[0-9][0-9][0-9].md"))
    expected_names = {f"{identifier}.md" for identifier in EXPECTED_PAPER_IDS}
    if len(expected_names) != EXPECTED_PAPER_PAGES:
        errors.append("论文编号清单与预期篇数不一致")
    actual_names = {path.name for path in paper_pages}
    if actual_names != expected_names:
        errors.append(
            "论文页面集合不完整；"
            f"缺少={sorted(expected_names - actual_names)}；"
            f"多余={sorted(actual_names - expected_names)}"
        )
    index_path = paper_dir / "README.md"
    if not index_path.is_file():
        errors.append("缺少论文与技术报告解读索引")
    else:
        index_text = index_path.read_text(encoding="utf-8")
        index_names = re.findall(r"\]\((P[0-9]{3}\.md)\)", index_text)
        indexed_names = set(index_names)
        if indexed_names != expected_names or len(index_names) != len(expected_names):
            errors.append(
                "论文与技术报告解读索引必须覆盖每篇且不重复；"
                f"缺少={sorted(expected_names - indexed_names)}；"
                f"多余={sorted(indexed_names - expected_names)}；"
                f"链接数量={len(index_names)}"
            )
    for page in paper_pages:
        text = page.read_text(encoding="utf-8")
        title = re.search(r"^# [^\n]+\n", text, flags=re.MULTILINE)
        resource_line = text[title.end():].lstrip().splitlines()[0] if title else ""
        if not re.match(r"\[(?:论文|技术报告|公司研究入口)(?:（v\d+）)?\]\(https?://", resource_line):
            errors.append(f"论文与项目链接应置于标题下：{page.relative_to(ROOT)}")
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
        and (ROOT / "技术与研究" / "论文逐篇解读" / "论文原图") in path.parents
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
    for title, (papers, projects) in EXPECTED_TRACK_COUNTS.items():
        rows = [line for line in readme.splitlines() if line.startswith(f"| [{title}](")]
        if len(rows) != 1 or len(rows[0].split("|")) != 4:
            errors.append(f"README技术方向应为两列表格且入口唯一：{title}")
            continue
        target = re.search(r"\]\(([^)]+)\)", rows[0]).group(1)
        chapter = ROOT / unquote(target)
        expected = f"当前收录 **{papers}** 篇论文／技术报告、**{projects}** 个项目。"
        if not chapter.is_file() or expected not in chapter.read_text(encoding="utf-8"):
            errors.append(f"章节数量与公开数据不一致：{title}；expected={expected}")
    # Check homepage section links as well as target file existence.
    for target in re.findall(r"\]\(([^)]+)\)", readme):
        if "#" not in target or target.startswith(("https:", "http:")):
            continue
        path, fragment = target.split("#", 1)
        destination = ROOT / unquote(path) if path else ROOT / "README.md"
        if not destination.is_file():
            continue
        content = destination.read_text(encoding="utf-8")
        headings = re.findall(r"^#{1,6} (.+)$", content, re.MULTILINE)
        anchors = {re.sub(r"[^\w\-\s]", "", heading.lower()).replace(" ", "-") for heading in headings}
        anchors.update(re.findall(r'(?:id|name)="([^"]+)"', content))
        if unquote(fragment) not in anchors:
            errors.append(f"README章节链接不存在：{target}")


def check_readme_badges(readme: str, errors: list[str]) -> None:
    class Images(HTMLParser):
        def __init__(self):
            super().__init__()
            self.sources: list[str] = []

        def handle_starttag(self, tag, attrs):
            if tag == 'img':
                source = dict(attrs).get('src')
                if source:
                    self.sources.append(source)

    images = Images()
    images.feed(readme)
    named_colors = {
        'brightgreen', 'green', 'yellow', 'yellowgreen', 'orange', 'red',
        'blue', 'grey', 'lightgrey', 'blueviolet',
    }
    for source in images.sources:
        url = urlsplit(source)
        if url.hostname != 'komarev.com' or url.path != '/ghpvc/':
            continue
        params = parse_qs(url.query, keep_blank_values=True)
        colors = params.get('color', ['blue'])
        if len(colors) != 1 or not (
            colors[0] in named_colors or re.fullmatch(r'[0-9a-fA-F]{6}', colors[0])
        ):
            errors.append('README访问量徽章颜色无效：应使用受支持的颜色名或六位HEX颜色')
        if not params.get('username', [''])[0].strip():
            errors.append('README访问量徽章缺少统计标识username')


def main() -> None:
    errors: list[str] = []
    files = collect_files(errors)
    check_paths(files, errors)
    check_export_manifest(files, errors)
    check_markdown(files, errors)
    check_readme_counts(errors)
    check_readme_badges((ROOT / 'README.md').read_text(encoding='utf-8'), errors)
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
