export default function createReportObject(employeesList) {
  return {
    allEmployees: { ...employeesList }, // Aquí debería estar la coma
    getNumberOfDepartments() {
      return Object.keys(this.allEmployees).length;
    }
  };
}
