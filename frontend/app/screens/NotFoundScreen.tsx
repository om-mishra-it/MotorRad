// app/screens/NotFoundScreen.tsx
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const NotFoundScreen = () => {
  return (
    <View style={styles.container}>
      <Text>404 - Not Found</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
});

export default NotFoundScreen;
