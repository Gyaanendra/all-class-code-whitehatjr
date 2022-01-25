import * as React from 'react';
import { Image } from 'react-native'
import { Button, View, Text, TouchableOpacity, StyleSheet, Iamges } from 'react-native';
import { Audio } from 'expo-av';
import Til from '../components/Til';


export default class Joke extends React.Component{

   gotoHome=()=>{
    this.props.navigation.navigate('Screen1')
  }
render(){
  return(
    <View>
        <Til/>
         <TouchableOpacity 
            style = {css.button}
            onPress={()=>{
              this.gotoHome()
            }}>
              <Image style={css.img} source = {require('../images/dsafsaf.png')} />
          </TouchableOpacity>
            
         <Image style={css.img2} source = {require('../images/asdasdasd.png')} />
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
   width: 200,
   height: 200,
  
  },
 
})