import React, { useRef, useState, useEffect } from 'react'
import axios from 'axios'
import { axios_options } from './Util.jsx'
import Console from 'react-console-component'
import './JConsole.css'
import { v4 as uuidv4 } from 'uuid'


const JConsole = () => {

  const jconsole = useRef(null)
  const [uuid, setUuid] = useState(null)
  useEffect(() => {
    if(uuid == null)
    {
      axios(axios_options('/j/new_session', 'get')).then((res) => {
        setUuid(res.data.data)
        console.log(res.data.data)
      })
    }
  })


  function onChange(newValue) {
    console.log("change", newValue);
    const data = {
      uuid: uuid,
      command: newValue + "\n"
    }
    const options = axios_options('/j/repl', 'post', 'auth_json', data)
    axios(options).then((res) => {
      jconsole.current.log(res.data.result)
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
