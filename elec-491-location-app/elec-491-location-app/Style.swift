//
//  Style.swift
//  elec-491-location-app
//
//  Created by Doğukan on 22.02.2022.
//

import Foundation
import UIKit

class Style {
    
    static func nutritionPackButton(_ input:UIButton) {
        input.backgroundColor = UIColor.systemBlue
        input.setTitle("Nutrition Pack \n(Water, Chocolate, Dried fruits)", for: .normal)
        input.tintColor = UIColor.white
        input.layer.cornerRadius = 12.0
        input.titleLabel?.textAlignment = .center
    }
    
    static func firstAidKitButton(_ input:UIButton) {
        input.backgroundColor = UIColor.systemRed
        input.setTitle("First Aid Kit \n(Bandages, Antibiotics, Burn cream)", for: .normal)
        input.tintColor = UIColor.white
        input.layer.cornerRadius = 12.0
        input.titleLabel?.textAlignment = .center
    }
    
    static func infoLabel(_ input:UILabel!) {
        input.textColor = UIColor.black
        input.font = UIFont(name:"HelveticaNeue-Bold", size: 22.0)
    }
}
