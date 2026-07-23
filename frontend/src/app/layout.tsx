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
