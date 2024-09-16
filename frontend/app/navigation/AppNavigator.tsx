// app/navigation/AppNavigator.tsx
import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from '../screens/HomeScreen'; // You'll create this file next
import NotFoundScreen from '../screens/NotFoundScreen'; // You'll create this file next

const Stack = createStackNavigator();

const AppNavigator = () => (
  <Stack.Navigator initialRouteName="Home">
    <Stack.Screen name="Home" component={HomeScreen} />
    <Stack.Screen name="NotFound" component={NotFoundScreen} />
  </Stack.Navigator>
);

export default AppNavigator;
