import { Alert, Button, Label, TextInput } from "flowbite-react";
import { Link, useNavigate } from "react-router-dom";
import users from "../data/users.json";
import { useState } from "react";

const FormLogin = () => {
  const [userLogin, setUserLogin] = useState({});
  const [alertError, setAlerError] = useState(false);
  // eslint-disable-next-line no-unused-vars
  const navigate = useNavigate();

  const handleChange = ({ target }) => {
    const { name, value } = target;
    setUserLogin({
      ...userLogin,
      [name]: value
    });
  };

  const handleSubmit = (e) => {
    setAlerError(false);
    e.preventDefault();
    const { email, password } = userLogin;
    const user = users.find(user => user.email === email && user.password === password);
    if (user) {
      const userLoggedIn = { ...user, isLoggedIn: true };
      localStorage.setItem('user', JSON.stringify(userLoggedIn));
      return navigate('/');
    } else {
      setAlerError(true);
    }
  };

  return (
    <form className="flex flex-1 mx-auto max-w-md flex-col px-5 gap-4" onSubmit={handleSubmit}>
      <div className="text-center text-primario-c-500 mb-24">
        <h1 className="text-3xl">Bienvenidos</h1>
        <p>Tus pagos de manera fácil</p>
      </div>
      <div>
        <div className="mb-2 block">
          <Label
            htmlFor="email"
            value="E-mail"
          />
        </div>
        <TextInput
          id="email"
          name="email"
          placeholder="name@digitalwallet.com"
          required
          type="email"
          color={"secondary-c"}
          onChange={handleChange}
        />
      </div>
      <div>
        <div className="mb-2 block">
          <Label
            htmlFor="password"
            value="Contraseña"
          />
        </div>
        <TextInput
          id="password"
          name="password"
          placeholder="***********"
          required
          type="password"
          color={"secondary-c"}
          onChange={handleChange}
        />
      </div>
      <Button
        type="submit"
        className="bg-secondary-c enabled:hover:bg-secondary-c focus:ring-secondary-c dark:bg-secondary-c dark:enabled:hover:bg-secondary-c dark:focus:ring-secondary-c rounded-lg focus:ring-2"
      >
        Submit
      </Button>
      <p className="text-sm font-light text-gray-500 dark:text-gray-400">
          Todavía no tienes una cuenta? <Link to="/register" className="font-medium text-primary-600 hover:underline dark:text-primary-500">Registrate aquí</Link>
      </p>
      {alertError && (
        <Alert color="failure">
          <span>
            <p>
              Email o Contraseña incorrecto.
            </p>
          </span>
        </Alert>
      )}
      <div className="mt-16 mx-auto">
        <img src="./src/assets/icon-digital-wallet.png" alt="logo digital wallet"/>
      </div>
    </form>
  );
};

export default FormLogin;