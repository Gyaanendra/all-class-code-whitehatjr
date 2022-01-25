import * as React from 'react';
import { Button, View, Text, TouchableOpacity, StyleSheet ,Image } from 'react-native';
import { Audio } from 'expo-av';
import Appheader from '../components/AppHeader';
import db from '../config';


export default class HomeScreen extends React.Component{
  constructor() {
    super();
    this.state = {
      like: 0,
      dislike: 0,
    };
  }

  likeCount = () => {
    this.setState({ like: this.state.like + 1 });
  };
  dislikeCount = () => {
    this.setState({ dislike: this.state.dislike + 1 });
  };

  changeScreen = (screen) => {
    this.props.navigation.navigate(screen);
  };

   dislikePressed(){
  var dislike=db.ref('Rating'+'/');
  dislike.update({ 
    DislikedPressed: 1
  }) 
}

  likePressed(){
  var like=db.ref('Rating'+'/');
  like.update({ 
    LikedPressed: 1
  }) 
}
  render() {
    return (
      <View style={styles.viewStyle}>
     <View>
      <Appheader/>
      </View>
        <TouchableOpacity
          style={[styles.buttonStyle, { backgroundColor: 'magenta' }]}
          onPress={() => {
            this.changeScreen( 'Screen2');
          }}>
          <Text style={styles.textStyle}>Jokes</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.buttonStyle, { backgroundColor: 'indigo' }]}
          onPress={() => {
            this.changeScreen('Screen3');
          }}>
          <Text style={styles.textStyle}>Horoscope</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.buttonStyle, { backgroundColor: 'teal' }]}
          onPress={() => {
            this.changeScreen('Screen4');
          }}>
          <Text style={styles.textStyle}>Weather</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.buttonStyle, { backgroundColor: 'cyan' }]}
          onPress={() => {
            this.changeScreen('Screen5');
          }}>
          <Text style={styles.textStyle}>Top News</Text>
        </TouchableOpacity>

        <Text style={styles.textStyle2}>Rate Us</Text>

        <Text style={styles.likeT}>{this.state.like}</Text>
        <TouchableOpacity onPress={ this. likePress ,this.likeCount}>
          <Image
            style={styles.image2}
            source={require('../images/thumbsup.png')}
          />
        </TouchableOpacity>

        <Text style={styles.dislikeT}>{this.state.dislike}</Text>
        <TouchableOpacity onPress={ this.dislikePressed ,this.dislikeCount}>
          <Image
            style={styles.image1}
            source={require('../images/thumbsdown.png')}
          />
        </TouchableOpacity>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  viewStyle: {
    alignItems: 'center',
  },

  buttonStyle: {
    borderWidth: 1,
    alignItems: 'center',
    justifyContent: 'center',
    width: 180,
    height: 45,
    borderRadius: 10,
    marginBottom: 30,
  },

  textStyle: {
    fontSize: 20,
    fontWeight: 'bold',
    fontFamily: 'times',
  },

  textStyle2: {
    fontSize: 20,
    fontWeight: 'bold',
    fontFamily: 'times',
    marginBottom: 10,
  },

  image1: {
    width: 50,
    height: 50,
    marginTop: -55,
    marginLeft: 80,
  },
  image2: {
    width: 50,
    height: 50,
    marginLeft: -70,
  },

  likeT: {
    fontFamily: 'Comic Sans MS',
    fontSize: 15,
    marginLeft: -105,
    marginBottom: 10,
    fontWeight: 'bold',
  },

  dislikeT: {
    fontFamily: 'Comic Sans MS',
    fontSize: 15,
    marginLeft: 100,
    marginBottom: 80,
    marginTop: -80,
    fontWeight: 'bold',
  },
});
