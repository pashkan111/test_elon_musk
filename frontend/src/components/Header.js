import React, {useEffect, useState} from 'react'
import img from '../assets/spaceX-logo.png'
import { BiDotsVerticalRounded } from "react-icons/bi";

const navBar = [
    'Главная', 'Технология',
    'График полетов', 'Гарантии', 
    'О компании', 'Контакты']

function Header() {
    // const [navBar, setNavBar] = useState([])

    useEffect(() => {

    })
  return (
    <header>
        <div className="logo">
            <img src={img} alt="SpaceX Logo"/>
        </div>
        <nav>
            <ul>
            {navBar.map((el, i) => <li key={i}>
                    <a href="#">{el}</a>
                </li>)}
            </ul>
        </nav>
        <div className='points'>
            <BiDotsVerticalRounded/>
        </div>
      </header>
  )
}

export default Header