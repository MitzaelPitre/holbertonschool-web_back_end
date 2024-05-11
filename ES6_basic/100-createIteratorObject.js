export default function* createIteratorObject(report) {
  for (const department in report.allEmployees) {
    if (report.allEmployees.hasOwnProperty(department)) {
      const employees = report.allEmployees[department];
      for (const employee of employees) {
        yield employee;
      }
    }
  }
}
