import React from 'react';
import { AppRegistry } from 'react-native';
import MapScreen from '/Users/xwidener/Documents/StudyMaps/Study/app/mapScreen.js';  // Adjust the path if needed
import { name as appName } from '/Users/xwidener/Documents/StudyMaps/Study/app.json';

const App = () => <MapScreen />;

AppRegistry.registerComponent(appName, () => App);


