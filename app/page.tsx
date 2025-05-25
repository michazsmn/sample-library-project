import { Button } from "@/components/ui/button"


export default function Home() {
  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      
      <header className="row-start-1 flex items-center justify-between w-full">
        <h1 className="text-4xl font-bold">Sample Library</h1>
        <nav className="flex gap-4 text-xl">
          <a href="#" >Login</a>
          <a href="#" >Home</a>
        </nav>
      </header>
      <main className="flex flex-col gap-[32px] row-start-2 items-center sm:items-start">
        <h2 className="text-3xl font-bold">Modern Sample Library for Producers and Audio Enthusiasts</h2>
        <div className="flex flex-row gap-[16px] items-center justify-center w-full">
          <Button className="bg-gray-900 hover:bg-gray-800 text-white font-bold py-2 px-4 rounded" size={"lg"}>
            Explore
          </Button>
          <Button className="bg-gray-900 hover:bg-gray-800 text-white font-bold py-2 px-4 rounded" size={"lg"}>
            Login
          </Button>
        </div>
      </main>
      <footer className="row-start-3 flex gap-[24px] flex-wrap items-center justify-center">
        
      </footer>
    </div>
  );
}
