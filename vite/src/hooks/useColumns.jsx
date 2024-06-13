import { useMemo } from "react";

export const useColumns = () =>
  useMemo(
    () => [
      {
        accessorKey: "name.firstName",
        header: "First Name",
        size: 150,
      },
      {
        accessorKey: "name.lastName",
        header: "Last Name",
        size: 150,
      },
      {
        accessorKey: "grade",
        header: "Grade",
        size: 150,
      },
      {
        accessorKey: "city",
        header: "City",
        size: 150,
      },
    ],
    []
  );
