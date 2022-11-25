
Feature: Acceder al login de Ripley

  
  Scenario Outline: Login ripley
    Given entrar a la url <url>
    When doy click en "iniciar seccion"
    And ingreso mi rut <rut>
    And ingreso mi password <password>
    And doy click en "iniciar sesion"
    Then cerrar secion 
  Examples:
      
  |            url            | rut       | password   |  
  | https://simple.ripley.cl/ | 230814767 | Almendra7  | 