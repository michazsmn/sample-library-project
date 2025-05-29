import Link from 'next/link'
import React from 'react'
import { registration } from './actions'

export default function Register() {
  return (
    <div>              {/* @ts-ignore */}
      <form action={registration} className='flex flex-col justify-center items-center m-4 bg-black p-4 rounded-lg shadow-lg gap-3'>
        <input name='username' type='username' placeholder='Username' required className='w-xl p-4 text-2xl'/>
        <input name='email' type='email' placeholder='Email' required className='w-xl p-4 text-2xl'/>
        <input name='password' type='password' placeholder='Password' required className='w-xl p-4 text-2xl'/>
        <input name='passwordrepeat' type='passwordrepeat' placeholder='Repeat Password' required className='w-xl p-4 text-2xl'/>
        <div className='gap-[16px] flex flex-row items-center justify-center w-full mt-4'>
          <button type='submit' className='buttonHomePage'>Register</button>
        </div>
      </form>
    </div>
  )
}
