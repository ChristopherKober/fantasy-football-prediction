import React from 'react';
import './BasePage.scss'

import { TitleBar } from '../TitleBar/TitleBar';
import { NavPanel } from '../NavPanel/NavPanel';

export class BasePage extends React.Component {
    render() {
        return <div className="basepage">
            <TitleBar></TitleBar>
            <NavPanel></NavPanel>
        </div>;
    }    
}