import * as React from 'react';
import { Text, View, StyleSheet, Image } from 'react-native';

export default class Til extends React.Component {
  render() {
    return (
      <View style={css.view}>
        <Text style={css.text}>Read a joke </Text>
      </View>
    );
  }
}

const css = StyleSheet.create({
  view: {
    backgroundColor: 'red',
  },

  text: {
    padding: 20,
    textAlign: 'center',
    fontWeight: 'bold',
    color: 'white',
    fontSize: 20,
  },
});
