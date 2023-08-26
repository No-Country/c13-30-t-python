import { Button, Checkbox, Label, TextInput } from "flowbite-react";

const FormLogin = () => {
  return (
    <form className="flex flex-1 mx-auto max-w-md flex-col px-5 gap-4">
      <div className="text-center text-primario-c-500 mb-24">
        <h1 className="text-3xl">Bienvenidos</h1>
        <p>Tus pagos de manera fácil</p>
      </div>
      <div>
        <div className="mb-2 block">
          <Label
            htmlFor="email1"
            value="E-mail"
          />
        </div>
        <TextInput
          id="email1"
          placeholder="name@digitalwallet.com"
          required
          type="email"
          color={"secondary-c"}
        />
      </div>
      <div>
        <div className="mb-2 block">
          <Label
            htmlFor="password1"
            value="Contraseña"
          />
        </div>
        <TextInput
          id="password1"
          placeholder="***********"
          required
          type="password"
          color={"secondary-c"}
        />
      </div>
      <div className="flex items-center gap-2">
        <Checkbox id="remember" />
        <Label htmlFor="remember">
          Remember me
        </Label>
      </div>
      <Button
        type="submit"
        className="bg-secondary-c enabled:hover:bg-secondary-c focus:ring-secondary-c dark:bg-secondary-c dark:enabled:hover:bg-secondary-c dark:focus:ring-secondary-c rounded-lg focus:ring-2"
      >
        Submit
      </Button>
      <Button
        type="submit"
        outline
      >
        Submit
      </Button>
      <div className="mt-16 mx-auto">
        <img src="./src/assets/icon-digital-wallet.png" alt="logo digital wallet"/>
      </div>
    </form>
  );
};

export default FormLogin;