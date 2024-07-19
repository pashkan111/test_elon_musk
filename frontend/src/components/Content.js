import React from 'react'
import ContentItem from './ContentItem'

function Content({contentItems}) {
  return (
    <div className="content">
        {contentItems.map((el, i) => 
            <ContentItem key={i} contentItem={el}/>
        )}
    </div>
  )
}

export default Content