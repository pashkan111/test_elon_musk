import React from 'react'

function ContentItem({contentItem}) {
  const {value, description} = contentItem
  const descriptionItem = description.split('%')
  
  return (
    <div className="content-item">
        <p>{descriptionItem[0]}</p>
        <h2>{value}</h2>
        <p>{descriptionItem[1]}</p>
    </div>
  )
}

export default ContentItem