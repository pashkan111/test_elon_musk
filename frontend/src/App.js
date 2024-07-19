import React, {useState, useEffect} from 'react'
import './App.css';
import Header from './components/Header'
import Content from './components/Content';

// const navBarItems = [
//   {id: 1, title: 'Главная'},
//     {id: 2, title: 'Технология'},
//     {id: 3, title: 'График полетов'}, 
//     {id: 4, title: 'Гарантии'}, 
//     {id: 5, title: 'О компании'}, 
//     {id: 6, title: 'Контакты'}
// ]
// const contentItems = [
//   {value: '50%', description: 'гарантируем%безопасность'},
//   {value: '2001 г.', description: 'Календарик за%в подарок'},
//   {value: '597', description: 'путешествие%дней'},         
// ]

function App() {
  const [navBarItems, setNavBarItems] = useState([])
  const [contentItems, setContentItems] = useState([])
  const [error, setError] = useState(null)
  const [loading, setLoading] = useState(true)

  const fetchDataMenu = async() => {
    const response = await fetch('http://localhost:8000/api/menu/')
    if(!response.ok){
      throw new Error('Что-то пошло не так...')
    }
    const data = await response.json()

    const loadedMenu = []

    for(const key in data){
      loadedMenu.push({
        title: data[key].title
      })
    }
    setNavBarItems(loadedMenu)
  }

  const fetchDataContent = async() => {
    const response = await fetch('http://localhost:8000/api/advantages/')
    if(!response.ok){
      throw new Error('Что-то пошло не так...')
    }
    const data = await response.json()

    const loadedContent = []

    for(const key in data){
      loadedContent.push({
        value: data[key].value,
        description: data[key].description
      })
    }
    setContentItems(loadedContent)
  }
  

  useEffect(() => {
    const fetchData = async() => {
      try{
      setLoading(true);
      setError(null);
      await Promise.all([fetchDataMenu(),
      fetchDataContent()])
    }catch(err){
      setError(err)
    } finally{
      setLoading(false)
    }}

    fetchData()
  }, [])

  if (loading) return <div className='loading'>Loading...</div>;
  if (error) return <div className='error'>Error: {error.message}</div>;

  return (
    <main>
      <Header navBarItems={navBarItems}/>
      
      <div className='main'>
        <div className="title">
          <h1><span>ПУТЕШЕСТВИЕ</span> <br></br>на красную планету</h1>
          <div>
            <button>Начать путешествие</button>
          </div>
        </div>
        <Content contentItems={contentItems}/>
      </div>
    </main>
  );
}

export default App;
