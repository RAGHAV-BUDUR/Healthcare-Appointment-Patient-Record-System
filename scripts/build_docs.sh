#!/usr/bin/env bash
# Builds the three deliverables (.docx) from the Markdown sections in docs/.
# Used by the CD workflow on every merge to main; also works locally if pandoc is installed.
# Sections that are not merged yet are skipped, so the build never fails on a partial set.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="${1:-$ROOT/build}"
mkdir -p "$OUT"

build() {  # build <folder> <output name> <file>...
  local dir="$1" name="$2"; shift 2
  local present=()
  for f in "$@"; do [ -f "$ROOT/docs/$dir/$f" ] && present+=("$f"); done
  if [ ${#present[@]} -eq 0 ]; then echo "skip $name (no sections yet)"; return; fi
  ( cd "$ROOT/docs/$dir" && pandoc "${present[@]}" --resource-path=. -o "$OUT/$name" )
  echo "built $name from ${#present[@]} of $# sections"
}

build srs Team13_SRS.docx \
  01-introduction.md 02-overall-description.md 03-external-interfaces.md \
  04-1-auth-roles.md 04-2-patients.md 04-3-doctors-schedules.md 04-4-appointments.md \
  04-5-medical-records.md 04-6-notifications-reports.md 05-nfr.md 05-1-security.md \
  06-quality-acceptance.md 07-use-case-diagram.md 08-rtm.md

build sad Team13_SAD.docx \
  01-introduction.md 02-document-overview.md 03-1-goals-constraints.md 03-2-stakeholders.md \
  03-3-component-diagram.md 03-4-component-descriptions.md 03-5-architecture-pattern.md \
  03-6-tech-stack.md 03-7-risks.md 03-8-traceability.md 03-9-security-architecture.md \
  04-1-design-overview.md 04-2-seq-book-appointment.md 04-2-seq-consultation-prescription.md \
  04-3-api-appointment-service.md 04-3-api-medical-record-service.md 04-4-error-handling.md \
  04-5-ux-design.md 04-6-open-issues.md 05-appendices.md

TCS=()
if [ -d "$ROOT/docs/testplan/test-cases" ]; then
  while IFS= read -r f; do TCS+=("test-cases/$f"); done < <(ls "$ROOT/docs/testplan/test-cases" | grep '\.md$' | sort)
fi
build testplan Team13_TestPlan.docx \
  01-introduction.md 02-test-items.md 03-features-to-test.md 04-features-not-tested.md \
  05-approach.md 05-1-security-validation.md 06-environment.md 07-schedule.md \
  08-deliverables.md 09-roles.md 10-risks.md 11-assumptions.md 12-suspension.md \
  13-traceability.md 14-metrics-reporting.md 15-approvals.md "${TCS[@]}"
