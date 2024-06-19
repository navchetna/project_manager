import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import NavItemsConfig from "./config/NavItemsConfig";
import SidebarItemsConfig from "./config/SidebarItemsConfig";
import FormLayout from "./components/Forms/FormLayout";
import Layout1 from "./layouts/Layout1";
import Layout2 from "./layouts/Layout2";
import Layout3 from "./layouts/Layout3";
import { Layout } from "antd";
import TableBasic from "./components/Tables/TableBasic";
import TableAdvancedWithProviders from "./components/Tables/TableAdvanced";
// import VideoPlayer from "./components/VideoPlayer";

function App() {

  return (
    <>
      <div>
        <Layout1 />
        {/* <Layout2 /> */}
        {/* <Layout3 /> */}
        {/* <Navbar
          navigationItems={NavItemsConfig.navigationItems}
          menuItems={NavItemsConfig.menuItems}
          logoPath={NavItemsConfig.logoPath}
        /> */}
        {/* <Sidebar sidebarItems={SidebarItemsConfig.sidebarItems} /> */}
        {/* <TableAdvancedWithProviders /> */}
        {/* <TableBasic></TableBasic> */}
        {/* <VideoPlayer videoURL={"https://www.youtube.com/watch?v=Tk5bqlb5F4M"} /> */}
        {/* <FormLayout /> */}
      </div>
    </>
  );
}

export default App;
