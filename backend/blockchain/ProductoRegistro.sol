// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ProductoRegistro {
    mapping(bytes32 => bool) public registros;

    function registrarProducto(bytes32 hashProducto) public {
        registros[hashProducto] = true;
    }

    function verificarProducto(bytes32 hashProducto) public view returns (bool) {
        return registros[hashProducto];
    }
}
