import Car from './10-car';

export default class EVCar extends Car {
  constructor(brand, motor, color, range) {
    // Llama al constructor de la super clase (Car)
    super(brand, motor, color);

    // Crea las propiedades específicas de EVCar
    this._range = range;
  }

  cloneCar() {
    // Crea una nueva instancia de Car con las mismas propiedades
    return new Car(this._brand, this._motor, this._color);
  }
}
