import type { Metadata} from "next";
import Link from "next/link";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";


const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Sample Library",
  description: "by Michael Zusmanovskiy",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning className="h-full">
      <body className={`${geistSans.variable} ${geistMono.variable} antialiased h-full flex flex-col justify-between font-[family-name:var(--font-geist-sans)] min-h-screen`}>
        <header className="flex justify-between p-10 bg-black">
          <h1 className="text-5xl font-bold">Sample Library</h1>
          <nav className="flex gap-4 text-xl">
            <Link href="/login" className="headerLink">Login</Link>
            <Link href="/" className="headerLink">Home</Link>
          </nav>
        </header>
        <main className="flex flex-col gap-[32px] items-center">
          {children}
        </main>
        <footer className="h-6 bg-black">

        </footer>          
      </body>
    </html>
  );
}
