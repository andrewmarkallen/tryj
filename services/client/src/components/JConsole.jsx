import React, { useRef } from 'react'
import axios from 'axios'
import { axios_options } from './Util.jsx'
import Console from 'react-console-component'
import './JConsole.css'
import { v4 as uuidv4 } from 'uuid'


const JConsole = () => {

  const jconsole = useRef(null)

  function onChange(newValue) {
    console.log("change", newValue);
    const options = axios_options('/j', 'get')
    axios(options).then((res) => {
      jconsole.current.log(res.data)
      jconsole.current.return()})
  }

  return (
    <div>
    Hi
    <Console    ref={jconsole}
                handler={onChange}
                autofocus={true}
            />
    </div>
  )
}

export default JConsole
