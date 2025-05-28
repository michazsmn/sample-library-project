import Link from "next/link";

export default function Home() {
  return (
      <div className="flex flex-col gap-[32px] items-center mb-40">
        <h2 className="text-4xl font-bold">Modern Sample Library for Producers and Audio Enthusiasts</h2>
        <div className="flex flex-row gap-[16px] items-center justify-center w-full">
          <Link href="/explore" className="buttonHomePage">
            Explore
          </Link>
          <Link href="/login" className="buttonHomePage">
            Login
          </Link>
        </div>
      </div>

  );
}
