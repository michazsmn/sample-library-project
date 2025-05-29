import React from 'react'
import { signup } from '@/app/login/actions'
import Link from 'next/link'

export default function Login() {
  return (
    <div>
      {/* @ts-ignore */}
      <form action={signup} className='flex flex-col justify-center items-center m-4 bg-black p-4 rounded-lg shadow-lg gap-3'>
        <input name='email' type='email' placeholder='Email' required className='w-xl p-4 text-2xl'/>
        <input name='password' type='password' placeholder='Password' required className='w-xl p-4 text-2xl'/>
        <div className='gap-[16px] flex flex-row items-center justify-center w-full mt-4'>
          <button type='submit' className='buttonHomePage'>Login</button>
          <Link href="/register" className='buttonHomePage'>Register</Link>
        </div>
        
      </form>

    </div>
  )
}
