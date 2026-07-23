#!/usr/bin/env bash

set -Eeuo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$PROJECT_ROOT"

echo "========================================="
echo "ALPIP Phase 2.1 Pack 002"
echo "Frontend Foundation Initialization"
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
"frontend/src"
"frontend/src/app"
"frontend/src/components"
"frontend/src/components/ui"
"frontend/src/components/layout"
"frontend/src/features"
"frontend/src/hooks"
"frontend/src/lib"
"frontend/src/services"
"frontend/src/types"
"frontend/src/config"
"frontend/public"
"frontend/tests"
)


for dir in "${FRONTEND_DIRS[@]}"
do
    create_dir "$dir"
done


echo ""
echo "Creating Next.js foundation files..."


create_file "frontend/package.json"

cat > frontend/package.json <<'EOF'
{
  "name": "alpip-frontend",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  }
}
EOF


create_file "frontend/tsconfig.json"

cat > frontend/tsconfig.json <<'EOF'
{
  "compilerOptions": {
    "target": "ES2017",
    "lib": [
      "dom",
      "dom.iterable",
      "esnext"
    ],
    "allowJs": false,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true
  },
  "include": [
    "src"
  ]
}
EOF


create_file "frontend/next.config.ts"

cat > frontend/next.config.ts <<'EOF'
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  reactStrictMode: true
};

export default nextConfig;
EOF


echo ""
echo "Creating initial application files..."


create_file "frontend/src/app/layout.tsx"

cat > frontend/src/app/layout.tsx <<'EOF'
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "ALPIP",
  description: "Arabic Legal Intelligence Platform"
};

export default function RootLayout({
  children
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="ar">
      <body>{children}</body>
    </html>
  );
}
EOF


create_file "frontend/src/app/page.tsx"

cat > frontend/src/app/page.tsx <<'EOF'
export default function Home() {
  return (
    <main>
      <h1>ALPIP</h1>
      <p>Arabic Legal Intelligence Platform</p>
    </main>
  );
}
EOF


echo ""
echo "Pack 002-A completed successfully."
echo ""
echo "Creating frontend quality configuration..."


create_file "frontend/.env.example"

cat > frontend/.env.example <<'EOF'
# ALPIP Frontend Environment

NEXT_PUBLIC_APP_NAME=ALPIP
NEXT_PUBLIC_API_URL=http://localhost:8000
EOF


create_file "frontend/eslint.config.mjs"

cat > frontend/eslint.config.mjs <<'EOF'
import { defineConfig } from "eslint/config";

export default defineConfig([
  {
    ignores: [
      ".next",
      "node_modules"
    ]
  }
]);
EOF


create_file "frontend/.prettierrc"

cat > frontend/.prettierrc <<'EOF'
{
  "semi": true,
  "singleQuote": false,
  "tabWidth": 2,
  "trailingComma": "es5"
}
EOF


echo ""
echo "Creating frontend library structure..."


create_file "frontend/src/lib/utils.ts"

cat > frontend/src/lib/utils.ts <<'EOF'
export function cn(
  ...classes: Array<string | undefined | false>
): string {
  return classes.filter(Boolean).join(" ");
}
EOF


create_file "frontend/src/config/app.ts"

cat > frontend/src/config/app.ts <<'EOF'
export const APP_CONFIG = {
  name: "ALPIP",
  description:
    "Arabic Legal Intelligence Platform"
};
EOF


create_file "frontend/src/types/common.ts"

cat > frontend/src/types/common.ts <<'EOF'
export interface ApiResponse<T> {
  success: boolean;
  data?: T;
  message?: string;
}
EOF


echo ""
echo "Creating UI foundation..."


create_file "frontend/src/components/layout/AppShell.tsx"

cat > frontend/src/components/layout/AppShell.tsx <<'EOF'
interface AppShellProps {
  children: React.ReactNode;
}

export function AppShell({
  children
}: AppShellProps) {
  return (
    <div>
      {children}
    </div>
  );
}
EOF


create_file "frontend/src/components/ui/Placeholder.tsx"

cat > frontend/src/components/ui/Placeholder.tsx <<'EOF'
interface PlaceholderProps {
  text: string;
}

export function Placeholder({
  text
}: PlaceholderProps) {
  return (
    <div>
      {text}
    </div>
  );
}
EOF


echo ""
echo "Updating roadmap..."

if [ -f "docs/Master-Implementation-Roadmap.md" ]; then

cat >> docs/Master-Implementation-Roadmap.md <<'EOF'


## Pack 002 Progress

Status:

In Progress

Completed:

- Frontend architecture created
- Next.js foundation prepared
- TypeScript configuration created
- UI foundation started

EOF

fi


echo ""
echo "Pack 002-B completed successfully."
echo ""
echo "Running Pack 002 validation..."


VALIDATION_FAILED=0


REQUIRED_FRONTEND_DIRS=(
"frontend/src"
"frontend/src/app"
"frontend/src/components"
"frontend/src/components/ui"
"frontend/src/components/layout"
"frontend/src/lib"
"frontend/src/config"
"frontend/src/types"
)


for dir in "${REQUIRED_FRONTEND_DIRS[@]}"
do
    if [ -d "$dir" ]; then
        echo "OK directory: $dir"
    else
        echo "MISSING directory: $dir"
        VALIDATION_FAILED=1
    fi
done



REQUIRED_FRONTEND_FILES=(
"frontend/package.json"
"frontend/tsconfig.json"
"frontend/next.config.ts"
"frontend/src/app/layout.tsx"
"frontend/src/app/page.tsx"
"frontend/src/lib/utils.ts"
"frontend/src/config/app.ts"
"frontend/src/types/common.ts"
"frontend/src/components/layout/AppShell.tsx"
"frontend/src/components/ui/Placeholder.tsx"
)


for file in "${REQUIRED_FRONTEND_FILES[@]}"
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
    echo "PACK 002 COMPLETED SUCCESSFULLY"
    echo "Frontend foundation is ready."
    echo "========================================="


    if [ -f "docs/Master-Implementation-Roadmap.md" ]; then

cat >> docs/Master-Implementation-Roadmap.md <<'EOF'


## Pack 002 Final Status

Status:

Completed

Delivered:

- Next.js foundation
- TypeScript setup
- Frontend architecture
- Initial UI layer
- Configuration foundation

EOF

    fi


else

    echo "========================================="
    echo "PACK 002 FAILED"
    echo "Check missing items above."
    echo "========================================="

    exit 1

fi


echo ""
echo "Next commands:"
echo "git add ."
echo "git commit -m \"feat(frontend): initialize Next.js foundation\""
echo "git push"
