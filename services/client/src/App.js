import React from 'react';
import AceEditor from 'react-ace'
import './App.css';

function onChange(newValue) {
  console.log("change", newValue);
}

function App() {
  return (
    <div className="App">
      <AceEditor
          mode="java"
          theme="github"
          onChange={onChange}
          name="UNIQUE_ID_OF_DIV"
          editorProps={{ $blockScrolling: true }}
          setOptions={{
            enableBasicAutocompletion: true,
            enableLiveAutocompletion: true,
            enableSnippets: true
          }}
        />
    </div>
  );
}

export default App;
