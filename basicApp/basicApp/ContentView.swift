//
//  ContentView.swift
//  basicApp
//
//  Created by Andrew Kloecker on 6/9/21.
//

import SwiftUI


struct ContentView: View {
    @State var saying: String = "hey"
    
    var body: some View {
        VStack(alignment: .leading) {
            Text("Hello Selenium")
            Text("\(saying)")
            Button(action:{
                self.saying += "y"
            }, label: {
                Text("Add y")
            })
        }.padding()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        Group {
            ContentView()
        }
    }
}
