import * as React from 'react';
import { Image } from 'react-native'
import { Button, View, Text, TouchableOpacity, StyleSheet, Images } from 'react-native';
import { Audio } from 'expo-av';
import Horoscope from '../components/asd';


export default class Horo extends React.Component{

   gotoHome=()=>{
    this.props.navigation.navigate('Screen1')
  }
render(){
  return(
    <View>
        <Horoscope/>
         <TouchableOpacity 
            style = {css.button}
            onPress={()=>{
              this.gotoHome()
            }}>
              <Image style={css.img} source = {require('../images/dsafsaf.png')} />
          </TouchableOpacity>

          <Image style={css.img2}  source ={require('../images/asdf.png')}/>

        <Text style={css.text}></Text>
    </View>
  )
}
}


const css = StyleSheet.create({
  text: {
    color: 'black',
    textAlign: 'center',
    margin: 100,
    fontWeight: 'bold',
    fontSize: 30,
  },

  button:{
    justifyContent : 'center',
    alignSelf : 'left',
    marginTop:10,
      
  },

  img:{
   width: 80,
   height:80,
   backgroundColor:'white',
  },

  img2:{
   width: 340,
   height:340,
 
  },
 
})