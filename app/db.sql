-- Insertar marcas de automóviles de lujo (deportivos)
INSERT INTO brand (name, logo_url, is_car)
VALUES 
    ('Ferrari', 'https://example.com/ferrari_logo.png', true),
    ('Lamborghini', 'https://example.com/lamborghini_logo.png', true),
    ('Porsche', 'https://example.com/porsche_logo.png', true);

-- Insertar marcas de motocicletas de lujo (deportivas)
INSERT INTO brand (name, logo_url, is_car)
VALUES
    ('Ducati', 'https://example.com/ducati_logo.png', false),
    ('BMW Motorrad', 'https://example.com/bmw_motorrad_logo.png', false),
    ('KTM', 'https://example.com/ktm_logo.png', false);


-- Insertar más marcas de automóviles de lujo (deportivos)
INSERT INTO brand (name, logo_url, is_car)
VALUES 
    ('Aston Martin', 'https://example.com/aston_martin_logo.png', true),
    ('McLaren', 'https://example.com/mclaren_logo.png', true),
    ('Bugatti', 'https://example.com/bugatti_logo.png', true),
    ('Jaguar', 'https://example.com/jaguar_logo.png', true),
    ('Audi Sport', 'https://example.com/audi_sport_logo.png', true);

-- Insertar más marcas de motocicletas de lujo (deportivas)
INSERT INTO brand (name, logo_url, is_car)
VALUES
    ('Aprilia', 'https://example.com/aprilia_logo.png', false),
    ('MV Agusta', 'https://example.com/mv_agusta_logo.png', false),
    ('Suzuki GSX-R', 'https://example.com/suzuki_gsxr_logo.png', false),
    ('Honda CBR', 'https://example.com/honda_cbr_logo.png', false),
    ('Yamaha YZF', 'https://example.com/yamaha_yzf_logo.png', false);


-- Insertar 20 filas de datos de carros deportivos
INSERT INTO vehicles (brand, model, year, motor, traction, speedMax, power, stock, type, price, urlImage)
VALUES
    ('Tesla', 'Roadster', 2023, 'Eléctrico', 'Trasera', 250, 1000, 2, 'Deportivo', 200000, 'https://ejemplo.com/teslaroadster.jpg'),
    ('Jaguar', 'F-Type', 2022, 'V6', 'Trasera', 300, 380, 5, 'Deportivo', 95000, 'https://ejemplo.com/jaguarftype.jpg'),
    ('Audi', 'R8', 2023, 'V10', 'Trasera', 330, 562, 4, 'Deportivo', 160000, 'https://ejemplo.com/audir8.jpg'),
    ('Mercedes-Benz', 'AMG GT', 2022, 'V8', 'Trasera', 320, 523, 6, 'Deportivo', 140000, 'https://ejemplo.com/mercedesamggt.jpg'),
    ('Lotus', 'Evora', 2023, 'V6', 'Trasera', 280, 416, 3, 'Deportivo', 110000, 'https://ejemplo.com/lotusevora.jpg'),
    ('Alfa Romeo', '4C', 2022, 'Inline-4', 'Trasera', 160, 237, 2, 'Deportivo', 70000, 'https://ejemplo.com/alfaromeo4c.jpg'),
    ('Nissan', 'GT-R', 2023, 'V6', 'Integral', 315, 565, 8, 'Deportivo', 120000, 'https://ejemplo.com/nissangtr.jpg'),
    ('Maserati', 'GranTurismo', 2022, 'V8', 'Trasera', 185, 454, 4, 'Deportivo', 130000, 'https://ejemplo.com/maseratigranturismo.jpg'),
    ('Subaru', 'BRZ', 2023, 'Flat-4', 'Trasera', 220, 228, 5, 'Deportivo', 30000, 'https://ejemplo.com/subarubrz.jpg'),
    ('Chevrolet', 'Camaro', 2022, 'V8', 'Trasera', 275, 455, 6, 'Deportivo', 50000, 'https://ejemplo.com/chevroletcamaro.jpg'),
    ('Porsche', 'Cayman', 2023, 'Flat-4', 'Trasera', 290, 300, 4, 'Deportivo', 70000, 'https://ejemplo.com/porschecayman.jpg'),
    ('Ford', 'GT', 2022, 'V6', 'Trasera', 216, 647, 2, 'Deportivo', 500000, 'https://ejemplo.com/fordgt.jpg'),
    ('Lexus', 'LC 500', 2023, 'V8', 'Trasera', 471, 471, 3, 'Deportivo', 92000, 'https://ejemplo.com/lexuslc500.jpg'),
    ('Acura', 'NSX', 2022, 'V6', 'Integral', 307, 573, 2, 'Deportivo', 160000, 'https://ejemplo.com/acuransx.jpg'),
    ('McLaren', 'Artura', 2023, 'V6', 'Trasera', 205, 671, 2, 'Deportivo', 300000, 'https://ejemplo.com/mclarenartura.jpg'),
    ('Ferrari', 'F8 Tributo', 2022, 'V8', 'Trasera', 340, 710, 3, 'Deportivo', 300000, 'https://ejemplo.com/ferrarif8tributo.jpg'),
    ('Bugatti', 'Chiron', 2023, 'W16', 'Integral', 261, 1479, 1, 'Deportivo', 3000000, 'https://ejemplo.com/bugattichiron.jpg'),
    ('Koenigsegg', 'Jesko', 2022, 'V8', 'Trasera', 330, 1280, 1, 'Deportivo', 2800000, 'https://ejemplo.com/koenigseggjesko.jpg'),
    ('Pagani', 'Huayra', 2023, 'V12', 'Trasera', 230, 791, 2, 'Deportivo', 2800000, 'https://ejemplo.com/paganihuayra.jpg'),
    ('Lamborghini', 'Aventador', 2022, 'V12', 'Integral', 350, 759, 2, 'Deportivo', 400000, 'https://ejemplo.com/lamborghiniaventador.jpg');


-- Insertar 20 filas de datos de motos deportivas
-- Insertar 20 filas de datos de motos deportivas con is_deleted en false
INSERT INTO sport_motorcycles (brand, model, year, cylinder, speedMax, stock, price, urlImage, is_deleted)
VALUES
    ('Ducati', 'Panigale V4', 2023, 4, 200, 5, 30000, 'https://ejemplo.com/ducatipanigalev4.jpg', false),
    ('Yamaha', 'YZF-R1', 2022, 4, 185, 8, 22000, 'https://ejemplo.com/yamahayzfr1.jpg', false),
    ('Kawasaki', 'Ninja ZX-10R', 2023, 4, 186, 6, 25000, 'https://ejemplo.com/kawasakininjazx10r.jpg', false),
    ('Honda', 'CBR1000RR', 2022, 4, 186, 7, 23000, 'https://ejemplo.com/hondacbr1000rr.jpg', false),
    ('BMW', 'S1000RR', 2023, 4, 186, 5, 28000, 'https://ejemplo.com/bmws1000rr.jpg', false),
    ('Suzuki', 'GSX-R1000', 2022, 4, 186, 6, 21000, 'https://ejemplo.com/suzukigsxr1000.jpg', false),
    ('Aprilia', 'RSV4', 2023, 4, 201, 4, 32000, 'https://ejemplo.com/apriliarsv4.jpg', false),
    ('Triumph', 'Daytona 765', 2022, 3, 160, 5, 18000, 'https://ejemplo.com/triumphdaytona765.jpg', false),
    ('KTM', 'RC 390', 2023, 1, 170, 8, 8000, 'https://ejemplo.com/ktmrc390.jpg', false),
    ('MV Agusta', 'F4 RR', 2022, 4, 186, 3, 35000, 'https://ejemplo.com/mvagustaf4rr.jpg', false),
    ('Harley-Davidson', 'Sportster Iron 883', 2023, 2, 120, 10, 12000, 'https://ejemplo.com/harleydavidsonsportsteriron883.jpg', false),
    ('Ducati', 'Monster 1200', 2022, 2, 160, 5, 17000, 'https://ejemplo.com/ducatimonster1200.jpg', false),
    ('Yamaha', 'MT-09', 2023, 3, 140, 7, 11000, 'https://ejemplo.com/yamahamt09.jpg', false),
    ('Kawasaki', 'Z900', 2022, 4, 140, 6, 13000, 'https://ejemplo.com/kawasakiz900.jpg', false),
    ('Honda', 'CB650R', 2023, 4, 135, 8, 9000, 'https://ejemplo.com/hondacb650r.jpg', false),
    ('BMW', 'F 900 R', 2022, 2, 140, 5, 15000, 'https://ejemplo.com/bmwf900r.jpg', false),
    ('Suzuki', 'SV650', 2023, 2, 125, 9, 8000, 'https://ejemplo.com/suzukisv650.jpg', false),
    ('Aprilia', 'Tuono V4', 2022, 4, 175, 4, 28000, 'https://ejemplo.com/apriliatuonov4.jpg', false),
    ('Triumph', 'Street Triple RS', 2023, 3, 165, 6, 17000, 'https://ejemplo.com/triumphstreettriplers.jpg', false),
    ('KTM', 'Duke 390', 2022, 1, 167, 8, 7000, 'https://ejemplo.com/ktmduke390.jpg', false);
