import React from 'react';
import './App.css';
import { NavPanel } from './common/navpanel/navpanel';
import { TitleBar } from './common/titlebar/titlebar';

function App() {
  return (
    <div className="App">
      <TitleBar></TitleBar>
      <NavPanel></NavPanel>
    </div>
  );
}

export default App;
