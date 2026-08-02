import React, { useState } from 'react'

const Button = () => {

    const [count, setCount] = useState(0)

    const addCount = ()=>{
        setCount(count+1)
    }

    const subCount = () => {
        setCount(count-1)
    }

  return (
    <>
        <button onClick={addCount}>+</button>
        <p>{count}</p>
        <button onClick={subCount}>-</button>
    </>
  )
}

export default Button
