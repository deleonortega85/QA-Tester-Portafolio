class pantalla {
//selectores de la pantalla de login
    login = {
            usuario : '[data-test="username"]',
            clave : '[data-test="password"]',
            btn_ingresar: '[data-test="login-button"]',
            msg_locked: 'Epic sadface: Sorry, this user has been locked out.', 
            msg_no: 'Epic sadface: Username and password do not match any user in this service',
            msg_title: 'Swag Labs',
            sel_title: '[data-test="error"]'
    }

//selectores de la pantalla menu    
    menu = {
        icon_burger: '#react-burger-menu-btn',
        btn_logout : '[data-test="logout-sidebar-link"]'
    }
//selectores de la pantalla de productos    
    productos = {
        producto : '',
        carrito : ''
    }
}
// habilitar los datos para los test
module.exports = new pantalla();