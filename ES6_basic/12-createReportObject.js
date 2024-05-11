export default function createReportObject(employeesList) {
  return {
    allEmployees: { ...employeesList }, // Coma añadida aquí
    getNumberOfDepartments() {
      return Object.keys(this.allEmployees).length;
    }
  };
}
