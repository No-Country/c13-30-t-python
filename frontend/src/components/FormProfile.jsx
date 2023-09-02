import { Button, Label, Select, TextInput } from "flowbite-react";
import { HiMail } from "react-icons/hi";
import countriesCode from "../data/code_country.json";

const FormProfile = () => {
  console.log(countriesCode);
  return (
    <>
      <div className="max-w-3xl">
        <div className="text-primario-c-500 mb-4">
          <h1 className="text-3xl">Datos personales</h1>
        </div>
        <form className="flex flex-1 mx-auto flex-col gap-4">
            <div className="flex">
              <div className="mb-2 mr-3 flex-1">
                <Label
                  htmlFor="name"
                  value="Nombre (s)"
                />
                <TextInput
                  id="name"
                  placeholder="John"
                  required
                  color={"secondary-c"}
                  type="text"
                />
              </div>
              <div className="mb-2 flex-1">
                <Label
                  htmlFor="last_name"
                  value="Apellido (s)"
                />
                <TextInput
                  id="last_name"
                  placeholder="Doe"
                  color={"secondary-c"}
                  type="text"
                />
              </div>
            </div>
            <div className="mb-2">
              <Label
                htmlFor="email1"
                value="E-mail"
              />
              <TextInput
                id="email1"
                placeholder="name@digitalwallet.com"
                type="email"
                rightIcon={HiMail}
                color={"secondary-c"}
              />
            </div>
            <div className="flex">
              <div className="mb-2 mr-3 flex-1">
                <Label
                  htmlFor="code_country_phone"
                  value="Código de países"
                />
                <Select
                  id="countries"
                  required
                  color="secondary-c"
                >
                  {countriesCode.map(({ country, code }) => (
                    <option value={code} key={code}>
                      {`(+${code}) ${country}`}
                    </option>
                  ))}
                </Select>
              </div>
              <div className="mb-2 flex-1">
                <Label
                  htmlFor="phone_number"
                  value="Celular"
                />
                <TextInput
                  id="phone_number"
                  placeholder="3126977415"
                  color="secondary-c"
                  type="number"
                />
              </div>
            </div>
            <div className="flex">
              <div className="mb-2 mr-3 flex-1">
                <Label
                  htmlFor="document_type"
                  value="Tipo de documento"
                />
                <Select
                  id="document_type"
                  color="secondary-c"
                >
                  <option>Cédula</option>
                  <option>Pasaporte</option>
                  <option>Identidad</option>
                </Select>
              </div>
              <div className="mb-2 flex-1">
                <Label
                  htmlFor="id"
                  value="Número de identificación"
                />
                <TextInput
                  id="id"
                  placeholder="1020497722"
                  color="secondary-c"
                  type="number"
                />
              </div>
            </div>

            <div className="flex">
            </div>
          <Button
            type="submit"
            className="bg-secondary-c enabled:hover:bg-secondary-c focus:ring-secondary-c dark:bg-secondary-c dark:enabled:hover:bg-secondary-c dark:focus:ring-secondary-c rounded-lg focus:ring-2"
          >
            Actualizar
          </Button>
        </form>
      </div>
      <div className="max-w-xl mt-4">
        <div className="text-primario-c-500 mb-4">
          <h1 className="text-3xl">Cambiar Contraseña</h1>
        </div>
        <form className="flex flex-1 mx-auto flex-col gap-4">
          <div className="max-w-sm">
            <div className="mb-2 block">
              <Label
                htmlFor="password"
                value="password"
              />
            </div>
            <TextInput
              id="password"
              required
              shadow
              placeholder="Nueva Contraseña"
              type="password"
              color="secondary-c"
            />
          </div>
        </form>
      </div>
      {/* <div className="mt-16 mx-auto">
        <img src="./src/assets/icon-digital-wallet.png" alt="logo digital wallet"/>
      </div> */}
    </>
  );
};

export default FormProfile;