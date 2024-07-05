import {
  DesktopOutlined,
  FileOutlined,
  PieChartOutlined,
  TeamOutlined,
  UserOutlined,
} from "@ant-design/icons";

function getItem(label, key, icon, children) {
  return {
    key,
    icon,
    children,
    label,
  };
}

const sidebarItems = [
  getItem("Students", "1", <PieChartOutlined />),
  getItem("Mentors", "2", <FileOutlined />),
  getItem("Enterprises", "3", <PieChartOutlined />),
  getItem("Colleges", "4", <TeamOutlined />),
  getItem("Edit Entities", "5", <UserOutlined />),
];

export default { sidebarItems };
