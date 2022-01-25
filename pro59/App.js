import React, { Component } from 'react';
import { Button, View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import { Audio } from 'expo-av';
import { createAppContainer, createSwitchNavigator } from 'react-navigation';
import HomeScreen from './Screen/HomeScreen';
import Joke from './Screen/Joke';
import Horo from './Screen/Horoscope';
import Wea from './Screen/Wea';
import Top  from './Screen/Top'

export default class App extends Component {
  render() {
    return (
      <View>
        <AppContainer />
      </View>
    );
  }
}



var AppNavigator = createSwitchNavigator({
  Screen1: HomeScreen,
  Screen2: Joke,
  Screen3: Horo,
  Screen4: Wea,
  Screen5: Top,
  

});

const AppContainer = createAppContainer(AppNavigator);
