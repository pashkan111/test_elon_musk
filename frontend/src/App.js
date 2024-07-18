import React from 'react'
import './App.css';
import planetImg from './assets/planet.png'
import Header from './components/Header'


//header
//main: background, planet with text, cart with text

function App() {
  return (
    <body>
      <Header/>
        <main>
        <div className="title">
                <h1><span>ПУТЕШЕСТВИЕ</span> <br></br>на красную планету</h1>
                <div>
                  <button>Начать путешествие</button>
                </div>
        </div>
        <div className="content">
            <div className="content-item">
                <p>Мы</p>
                <h2>1</h2>
                <p>на рынке</p>
            </div>
            <div className="content-item">
            <p>гарантируем</p>
                <h2>50%</h2>
                <p>безопасность</p>
            </div>
            <div className="content-item">
                <p>Календарик за</p>
                <h2>2001 г.</h2>
                <p>в подарок</p>
            </div>
            <div className="content-item">
            <p>путешествие</p>
                <h2>597</h2>
                <p>дней</p>
            </div>
        </div>
        </main>
    </body>
  );
}

export default App;
