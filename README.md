# ldd-evals

Behavioral evals for the linter-driven-development plugins in
[buzzdan/ai-coding-rules](https://github.com/buzzdan/ai-coding-rules). Each
case runs an agent with a plugin installed over a deliberately bad fixture
project and grades what the agent did. Every run spends real money. Nobody
installs this repository.

## Dependency direction

This repository depends on the plugin repository. The plugin repository never
depends on this one: no submodule, no generated file, nothing a user installs.
The plugin repository carries only a two-line pointer README under the plugin's
`evals/` directory and a convenience script that clones this repository.

Every baseline records the plugin commit and version it measured. A run names
its plugin explicitly with `PLUGIN=<path to the plugin directory>`; without it,
the Go suite measures `../ai-coding-rules/go-linter-driven-development` and the
Python suite `../ai-coding-rules/python-linter-driven-development`.

## Layout

    Taskfile.yaml        build · test · lint · docs:check · includes go: and py:
    runner/              ldd-eval, the language-neutral runner (Go)
    go/                  the Go suite: go-mini, manifest, cases, scaffold, postcheck
    py/                  the Python suite: py-mini, the same 149 ids with Python anchors, cases, scaffold, postcheck
    baselines/           committed reference runs: <lang>-<plugin version>-<plugin sha>/
    results/             ignored; where runs land until one is promoted to baselines/
    scripts/             promote-baseline.sh, check-docs.sh
    docs/                conventions and the architecture page

## Quick start

    task build                                  # bin/ldd-eval
    task go:manifest                            # manifest against the fixture
    task go:graders                             # regenerate review-full graders
    task go:run TIER=cheap CAP=1 CASE='trigger-*' PLUGIN=/path/to/go-linter-driven-development
    task go:regrade OUT=baselines/go-2.11.0-c78b55f TIER=cheap PLUGIN=...
    task py:manifest && task py:graders          # the Python suite's twins of the two checks
    task py:run TIER=cheap CAP=1 CASE='trigger-*' PLUGIN=/path/to/python-linter-driven-development

`go:run` and `py:run` copy the cases, scaffold, postcheck helpers and fixture
into `<plugin>/evals/`, a path the plugin repository ignores, because the
built-in `claude plugin eval` gate expects cases below the plugin directory.
The agent model is pinned to `MODEL` (default `claude-sonnet-5`) and every run
carries a cost cap `CAP` in USD. The Python suite's postchecks need `ruff`,
`mypy` (with pytest importable), `pytest`, `uvx` and `jq` on PATH beside `task`.

## Baselines

Verdicts are always committed. Traces are committed once per baseline as one
`traces.tar.zst`; unpack it beside the verdicts before `task go:regrade`.
Scaffolds are not committed, so graders that read the working tree report
"needs the kept scaffold" when regraded from a clone. Experiments stay in the
ignored `results/` directory.

How the evals work is documented in the plugin repository, starting at
[docs/index.md](https://github.com/buzzdan/ai-coding-rules/blob/main/docs/index.md).
This repository's own docs start at [docs/index.md](docs/index.md).
