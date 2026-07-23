#!/usr/bin/env bash

set -Eeuo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$PROJECT_ROOT"

echo "========================================="
echo "ALPIP Phase 2.6 Pack 012"
echo "Frontend Next.js Integration Foundation"
echo "========================================="


create_dir() {
    mkdir -p "$1"
    echo "Created directory: $1"
}


create_file() {
    if [ ! -f "$1" ]; then
        touch "$1"
        echo "Created file: $1"
    else
        echo "Exists: $1"
    fi
}


echo ""
echo "Creating frontend architecture..."


FRONTEND_DIRS=(
"frontend/src/app"
"frontend/src/components"
"frontend/src/components/ui"
"frontend/src/components/layout"
"frontend/src/lib"
"frontend/src/lib/api"
"frontend/src/config"
"frontend/src/hooks"
"frontend/src/types"
"frontend/src/tests"
)


for dir in "${FRONTEND_DIRS[@]}"
do
    create_dir "$dir"
done



echo ""
echo "Creating frontend package files..."


FRONTEND_FILES=(
"frontend/src/app/layout.tsx"
"frontend/src/app/page.tsx"
"frontend/src/components/ui/index.ts"
"frontend/src/components/layout/index.ts"
"frontend/src/lib/api/index.ts"
"frontend/src/config/index.ts"
"frontend/src/hooks/index.ts"
"frontend/src/types/index.ts"
)


for file in "${FRONTEND_FILES[@]}"
do
    create_file "$file"
done



echo ""
echo "Creating frontend configuration..."


cat > frontend/src/config/index.ts <<'EOF'
export const APP_CONFIG = {

  name: "ALPIP",

  version: "2.6",

  apiBaseUrl:
    process.env.NEXT_PUBLIC_API_URL ||
    "http://localhost:8000"

};
EOF



echo ""
echo "Creating API client foundation..."


cat > frontend/src/lib/api/client.ts <<'EOF'
export class ApiClient {


  constructor(
    private baseUrl: string
  ) {}



  async get(
    path: string
  ) {

    const response =
      await fetch(
        this.baseUrl + path
      );


    return response.json();

  }

}
EOF



cat > frontend/src/lib/api/index.ts <<'EOF'
import { APP_CONFIG } from "@/config";


export const apiClient =
  new (require("./client").ApiClient)(
    APP_CONFIG.apiBaseUrl
  );
EOF



echo ""
echo "Creating application layout..."


cat > frontend/src/app/layout.tsx <<'EOF'
export default function RootLayout(
  {
    children,
  }: {
    children: React.ReactNode
  }
) {

  return (

    <html lang="ar">

      <body>

        {children}

      </body>

    </html>

  );

}
EOF



echo ""
echo "Creating home page..."


cat > frontend/src/app/page.tsx <<'EOF'
export default function Home() {

  return (

    <main>

      <h1>
        ALPIP
      </h1>

      <p>
        Arabic Legal Intelligence Platform
      </p>

    </main>

  );

}
EOF



echo ""
echo "Pack 012-A completed successfully."
echo ""
echo "Creating UI component foundation..."


create_file "frontend/src/components/ui/Button.tsx"

cat > frontend/src/components/ui/Button.tsx <<'EOF'
type ButtonProps = {

  label: string;

  onClick?: () => void;

};


export default function Button(
  {
    label,
    onClick
  }: ButtonProps
) {

  return (

    <button
      onClick={onClick}
    >

      {label}

    </button>

  );

}
EOF



create_file "frontend/src/components/ui/Card.tsx"

cat > frontend/src/components/ui/Card.tsx <<'EOF'
type CardProps = {

  title: string;

  children: React.ReactNode;

};


export default function Card(
  {
    title,
    children
  }: CardProps
) {

  return (

    <section>

      <h2>
        {title}
      </h2>

      <div>
        {children}
      </div>

    </section>

  );

}
EOF



echo ""
echo "Creating dashboard layout..."


create_file "frontend/src/components/layout/Dashboard.tsx"

cat > frontend/src/components/layout/Dashboard.tsx <<'EOF'
export default function Dashboard(
  {
    children
  }: {
    children: React.ReactNode
  }
) {

  return (

    <div>

      <header>
        ALPIP Dashboard
      </header>


      <main>

        {children}

      </main>


    </div>

  );

}
EOF



echo ""
echo "Creating frontend extension points..."


create_dir "frontend/src/plugins"


create_file "frontend/src/plugins/index.ts"

cat > frontend/src/plugins/index.ts <<'EOF'
export interface FrontendPlugin {


  name: string;


  initialize(): void;


}
EOF



echo ""
echo "Creating authentication UI foundation..."


create_dir "frontend/src/features/auth"


create_file "frontend/src/features/auth/Login.tsx"

cat > frontend/src/features/auth/Login.tsx <<'EOF'
export default function Login(){

  return (

    <form>

      <input
        placeholder="Username"
      />


      <input
        placeholder="Password"
        type="password"
      />


      <button>
        Login
      </button>

    </form>

  );

}
EOF



echo ""
echo "Creating frontend tests..."


create_file "frontend/src/tests/config.test.ts"

cat > frontend/src/tests/config.test.ts <<'EOF'
import { APP_CONFIG } from "@/config";


test(
  "application config",
  () => {

    expect(
      APP_CONFIG.name
    ).toBe("ALPIP");

  }
);
EOF



echo ""
echo "Creating frontend architecture ADR..."


create_file "docs/adr/ADR-008-frontend-architecture.md"

cat > docs/adr/ADR-008-frontend-architecture.md <<'EOF'
# ADR-008: Frontend Architecture

## Status

Accepted


## Context

ALPIP requires a scalable user interface supporting multiple legal modules.


## Decision

Frontend will use:

- Next.js App Router
- Component based architecture
- API client abstraction
- Plugin UI extension points


## Benefits

- Modular UI
- Easier feature expansion
- Separation of concerns


## Consequences

All UI features must follow frontend module boundaries.
EOF



echo ""
echo "Updating roadmap..."

if [ -f "docs/Master-Implementation-Roadmap.md" ]; then

cat >> docs/Master-Implementation-Roadmap.md <<'EOF'


## Pack 012 Progress

Status:

In Progress

Completed:

- Next.js structure
- API client foundation
- UI components
- Dashboard layout
- Frontend plugin extension
- Authentication UI foundation
- ADR-008 created

EOF

fi


echo ""
echo "Pack 012-B completed successfully."
echo ""
echo "Running Pack 012 validation..."


VALIDATION_FAILED=0


REQUIRED_DIRS=(
"frontend/src/app"
"frontend/src/components"
"frontend/src/components/ui"
"frontend/src/components/layout"
"frontend/src/lib"
"frontend/src/lib/api"
"frontend/src/config"
"frontend/src/hooks"
"frontend/src/types"
"frontend/src/features/auth"
"frontend/src/plugins"
)


for dir in "${REQUIRED_DIRS[@]}"
do
    if [ -d "$dir" ]; then
        echo "OK directory: $dir"
    else
        echo "MISSING directory: $dir"
        VALIDATION_FAILED=1
    fi
done



REQUIRED_FILES=(
"frontend/src/app/layout.tsx"
"frontend/src/app/page.tsx"
"frontend/src/config/index.ts"
"frontend/src/lib/api/client.ts"
"frontend/src/lib/api/index.ts"
"frontend/src/components/ui/Button.tsx"
"frontend/src/components/ui/Card.tsx"
"frontend/src/components/layout/Dashboard.tsx"
"frontend/src/plugins/index.ts"
"frontend/src/features/auth/Login.tsx"
"frontend/src/tests/config.test.ts"
"docs/adr/ADR-008-frontend-architecture.md"
)


for file in "${REQUIRED_FILES[@]}"
do
    if [ -f "$file" ]; then
        echo "OK file: $file"
    else
        echo "MISSING file: $file"
        VALIDATION_FAILED=1
    fi
done



echo ""

if [ "$VALIDATION_FAILED" -eq 0 ]; then

    echo "========================================="
    echo "PACK 012 COMPLETED SUCCESSFULLY"
    echo "Frontend Integration Layer is ready."
    echo "========================================="


    if [ -f "docs/Master-Implementation-Roadmap.md" ]; then

cat >> docs/Master-Implementation-Roadmap.md <<'EOF'


## Pack 012 Final Status

Status:

Completed

Delivered:

- Next.js Frontend Foundation
- API Client Layer
- UI Component Foundation
- Dashboard Layout
- Authentication UI Foundation
- Frontend Plugin Extension Points
- Frontend Architecture ADR

EOF

    fi


else

    echo "========================================="
    echo "PACK 012 FAILED"
    echo "Review missing items above."
    echo "========================================="

    exit 1

fi


echo ""
echo "Next commands:"
echo "git add ."
echo "git commit -m \"feat(frontend): add nextjs integration foundation\""
echo "git push"
