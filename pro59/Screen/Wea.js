import * as React from 'react';
import { Image } from 'react-native'
import { Button, View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import { Audio } from 'expo-av';
import Appheader from '../components/AppHeader';
import Wea1 from '../components/Wea1.js';

export default class Wea extends React.Component{

   gotoHome=()=>{
    this.props.navigation.navigate('Screen1')
  }
render(){
  return(
    <View>
        <Wea1/>
         <TouchableOpacity 
            style = {css.button}
            onPress={()=>{
              this.gotoHome()
            }}>
              <Image style={css.img} source = {require('../images/dsafsaf.png')} />
          </TouchableOpacity>
            
      <Image style={css.img2} source = {require('../images/Screenshot_1.png')} />
    </View>
  )
}
}


const css = StyleSheet.create({
 

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
   width: 280,
   height:280,
   backgroundColor:'white',
  },
 
})