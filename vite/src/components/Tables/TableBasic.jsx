import { useEffect, useMemo, useState } from "react";
import {
  MaterialReactTable,
  useMaterialReactTable,
} from "material-react-table";
// import data from "../../config/TableDataConfig";
import { useColumns } from "../../hooks/useColumns";
import { writeData } from "../../actions/writeData";

const TableBasic = () => {
  const [data, setData] = useState([]);
  const [newData, setNewData] = useState([
    {
      grade: 5,
      name: "Faiz Feroz",
      city: "Houston",
    },
    {
      grade: 6,
      name: "Darren Nishan Patrao",
      city: "Toronto",
    },
  ]);
  const columns = useColumns();

  // const readData = async () => {
  //   // console.log("in fetchData");
  //   try {
  //     const response = await fetch(`${process.env.serverUrl}/read-data`, {
  //       method: "GET",
  //     });
  //     // console.log("response: ", response);
  //     const jsonData = await response.json();
  //     // console.log("jsonData: ", jsonData);
  //     setData(jsonData);
  //   } catch (err) {
  //     console.log("error: ", err);
  //   }
  // };

  // const writeData = async (data) => {
  //   try {
  //     const response = await fetch(`${serverUrl}/write-data`, {
  //       method: "GET",
  //       // headers: {
  //       //   "Content-Type": "application/json",
  //       // },
  //       // body: JSON.stringify({ newData }),
  //     });
  //     const jsonData = await response.json();
  //     console.log("Response from server:", jsonData);
  //   } catch (err) {
  //     console.log("error in writeData: ", err);
  //   }
  // };

  const table = useMaterialReactTable({
    columns,
    data, //data must be memoized or stable (useState, useMemo, defined outside of this component, etc.)
  });

  return (
    <>
      <div className="flex flex-col justify-center items-center">
        <MaterialReactTable table={table} />
        {/* <button onClick={readData}>Fetch Data</button> */}
        {/* <button onClick={writeData}>Write Data</button> */}
      </div>
    </>
  );
};

export default TableBasic;
