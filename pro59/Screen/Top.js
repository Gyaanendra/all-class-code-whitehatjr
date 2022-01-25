import * as React from 'react';
import { Image } from 'react-native'
import { Button, View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import { Audio } from 'expo-av';
import News from '../components/news';


export default class Top extends React.Component{

   gotoHome=()=>{
    this.props.navigation.navigate('Screen1')
  }
render(){
  return(
    <View>
        <News />
         <TouchableOpacity 
            style = {css.button}
            onPress={()=>{
              this.gotoHome()
            }}>
              <Image style={css.img} source = {require('../images/dsafsaf.png')} />
          </TouchableOpacity>

        <Text style={css.text}> Covid live: PM Modi to address the nation at 5pm today</Text>

         <Text style={css.text}> Covid-19: 7% fatality rate last week is Bengaluru s highest ever this year</Text>

          <Text style={css.text}> Central Bank, IOB may be taken up for privatisation</Text>

       
    </View>
  )
}
}


const css = StyleSheet.create({
  text: {
    color: 'black',
    textAlign: 'left',
     alignSelf : 'left',
    margin: 10,
    fontWeight: 'bold',
    fontSize: 16,
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
 
})