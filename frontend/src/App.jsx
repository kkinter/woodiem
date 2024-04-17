import React from "react";
import { Grid, GridItem } from "@chakra-ui/react";
import Sidebar from "./components/SideBar";
import NavBar from "./components/NavBar";

function App() {
  return (
    <>
      <Grid
        templateColumns="100px 1fr 300px"
        templateRows="auto 1fr auto"
        minH="100vh"
      >
        <GridItem colSpan={3}>
          <NavBar />
        </GridItem>
        <GridItem rowSpan={2} bg="gold" p={4}>
          <Sidebar />
        </GridItem>
        <GridItem p={4}>{/* 메인 */}</GridItem>
        <GridItem rowSpan={2} bg="gray.100" p={4}>
          {/* ! */}
        </GridItem>
        <GridItem colSpan={3}></GridItem>
      </Grid>
    </>
  );
}

export default App;
