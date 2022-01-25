import React from 'react';
import {
  Text,
  View,
  StyleSheet,
  TextInput,
  TouchableOpacity,
  Image,
} from 'react-native';
import { Header } from 'react-native-elements';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import db from './words';

export default class App extends React.Component {
  constructor() {
    super();
    this.state = {
      text: '',
      displaytext: '',
      chunks:[],
    };
  }

  render() {
    return (
      <SafeAreaProvider>
        <View style={css.container}>
          <Header
            backgroundColor={'lightblue'}
            centerComponent={{
              text: 'Monkey chunky ',
              style: {
                color: 'white',
                fontSize: 20,
              },
            }}
          />
             
              <Image 
              source={{uri:'https://www.shareicon.net/data/128x128/2015/08/06/80805_face_512x512.png'}}
              style={css.image}
              />


          <TextInput
            onChangeText={(text) => {
              this.setState({
                text: text,
              });
            }}
            value={this.state.text}
            style={css.inputbox}
          />
          <TouchableOpacity
            style={css.gb}
            onPress={() => {
              this.setState({
               chunks:db[this.state.text].chunks
              });
            }}>
            <Text style={css.bt}>go</Text>
          </TouchableOpacity>
          <View>
          {this.state.chunks.map(item=>{
            return(
              <TouchableOpacity style={css.chunkbut}>
              <Text style={css.dist}>
            {item}
            </Text>
            </TouchableOpacity>
            )
          })}

          </View>
        </View>
      </SafeAreaProvider>
    );
  }
}

const css = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#b8b8b8',
  },

  inputbox: {
    marginTop: 100,
    width: '60%',
    textAlign: 'center',
    alignSelf: 'center',
    height: 40,
    borderWidth: 4,
  },

  gb: {
    width: '50%',
    height: 55,
    alignSelf: 'center',
    padding: 10,
    margin: 10,
  },

  bt: {
    textAlign: 'center',
    fontSize: 30,
    fontWeight: 'bold',
  },
  dist:{
     textAlign: 'center',
     fontSize: 30,
  },

  image:{
    width:150,
     height:150,
     alignSelf:'center'
  },

  chunkbut:{
  width:'60%',
  height:50,
  textAlign: 'center',
  alignSelf: 'center',
  margin:5,
  borderRadius:10,
  backgroundColor:'lime'

  },

});
