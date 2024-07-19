import React from 'react'
import img from '../assets/spaceX-logo.png'
import { BiDotsVerticalRounded } from "react-icons/bi";

function Header({navBarItems}) {
  return (
    <header>
        <div className="logo">
            <img src={img} alt="SpaceX Logo"/>
        </div>
        <nav>
            <ul>
                {navBarItems.map((el, i) => (
                    <li key={i}>
                        <a href="#">{el.title}</a>
                    </li>
                ))}
            </ul>
        </nav>
        <div className='points'>
            <BiDotsVerticalRounded/>
        </div>
      </header>
  )
}

export default Header